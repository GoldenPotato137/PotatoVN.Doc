import requests
import json

def get_ms_store_app_version(product_id: str, market: str = "US", locale: str = "en-US"):
    """
    使用 DisplayCatalog API 获取微软商店应用的最新版本号。
    这个版本修正了解析逻辑，从 'PackageFullName' 字段提取版本号。

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
        
        if "Products" in data and data["Products"]:
            product = data["Products"][0]
            if "DisplaySkuAvailabilities" in product and product["DisplaySkuAvailabilities"]:
                sku_availability = product["DisplaySkuAvailabilities"][0]
                sku = sku_availability.get("Sku")
                if sku and "Properties" in sku and sku["Properties"].get("Packages"):
                    # Packages 是一个列表，通常包含 x86, x64, arm64 等架构
                    # 它们的版本号一般是相同的，我们取第一个即可
                    package = sku["Properties"]["Packages"][0]
                    package_full_name = package.get("PackageFullName")
                    
                    if package_full_name:
                        # 字符串格式为: Name_Version_Architecture__Hash
                        # 例如: "37126GoldenPotato137.PotatoVN_1.9.3.0_x86__8vtbc0gbd4jey"
                        # 我们通过下划线分割，取第二个元素
                        parts = package_full_name.split('_')
                        if len(parts) > 1:
                            return parts[1] # 返回版本号 '1.9.3.0'

        return "版本号未在返回的数据中找到（新路径）。"

    except requests.exceptions.HTTPError as e:
        return f"请求失败，HTTP 错误: {e.response.status_code}. 响应内容: {e.response.text}"
    except requests.exceptions.RequestException as e:
        return f"请求发生网络错误: {e}"
    except (KeyError, IndexError, TypeError, json.JSONDecodeError) as e:
        return f"解析 JSON 失败或数据结构不匹配: {e}"


potatovn_id = "9P9CBKD5HR3W"
version = get_ms_store_app_version(potatovn_id, market="US", locale="en-us")
print(version)
