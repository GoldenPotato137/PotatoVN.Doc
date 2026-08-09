import requests
import json

def parse_version(version_str: str):
    """
    将 '1.10.2.0' 形式的版本号字符串转换为可比较的元组，如 (1, 10, 2, 0)。
    解析失败时返回 None。
    """
    try:
        return tuple(int(part) for part in version_str.split('.'))
    except ValueError:
        return None

def get_ms_store_app_version(product_id: str, market: str = "US", locale: str = "en-US"):
    """
    使用 DisplayCatalog API 获取微软商店应用的最新版本号。

    注意：商店目录会同时保留历史提交的旧包和最新提交的包。现在的自动发布流程
    提交的是 msixbundle（在目录中体现为 'PackageFullName' 带 'neutral_~' 的包，
    且排在旧的各架构包之后），因此不能只取第一个包，必须遍历所有
    'PackageFullName' 并取其中的最高版本号。

    :param product_id: 应用的 Product ID (例如 '9P9CBKD5HR3W')
    :param market: 市场代码 (例如 'US', 'CN')
    :param locale: 语言地区代码 (例如 'en-US', 'zh-CN')
    :return: 版本号字符串或错误信息
    """
    try:
        url = (
            f"https://displaycatalog.mp.microsoft.com/v7.0/products"
            f"?bigIds={product_id}"
            f"&market={market}"
            f"&locale={locale}"
            f"&languages={locale}"
            f"&MS-CV=DGU1mcuYo0WMMp+F.1"
        )

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        versions = []
        if "Products" in data and data["Products"]:
            for product in data["Products"]:
                for sku_availability in product.get("DisplaySkuAvailabilities", []):
                    sku = sku_availability.get("Sku") or {}
                    packages = (sku.get("Properties") or {}).get("Packages") or []
                    for package in packages:
                        package_full_name = package.get("PackageFullName")
                        if not package_full_name:
                            continue
                        # 字符串格式为: Name_Version_Architecture[_ResourceId]__Hash
                        # 例如: "37126GoldenPotato137.PotatoVN_1.9.3.0_x86__8vtbc0gbd4jey"
                        # 或 bundle: "37126GoldenPotato137.PotatoVN_1.10.2.0_neutral_~_8vtbc0gbd4jey"
                        # 我们通过下划线分割，取第二个元素
                        parts = package_full_name.split('_')
                        if len(parts) > 1:
                            version = parse_version(parts[1])
                            if version:
                                versions.append(version)

        if versions:
            # 商店目录中混有历史旧包，最高版本号才是当前对外提供的版本
            latest = max(versions)
            return '.'.join(str(part) for part in latest)

        return "版本号未在返回的数据中找到。"

    except requests.exceptions.HTTPError as e:
        return f"请求失败，HTTP 错误: {e.response.status_code}. 响应内容: {e.response.text}"
    except requests.exceptions.RequestException as e:
        return f"请求发生网络错误: {e}"
    except (KeyError, IndexError, TypeError, json.JSONDecodeError) as e:
        return f"解析 JSON 失败或数据结构不匹配: {e}"


potatovn_id = "9P9CBKD5HR3W"
version = get_ms_store_app_version(potatovn_id, market="US", locale="en-us")
print(version)
