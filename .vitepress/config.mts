import { defineConfig } from 'vitepress'
// import {
//   GitChangelog,
//   GitChangelogMarkdownSection,
// } from '@nolebase/vitepress-plugin-git-changelog/vite'
import SideBar from "./SideBar";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  // 由于StackBlitz Web Publisher的git版本太老，不支持Git Changelog插件，本分支禁用Git Changelog插件
  // Git Changelog
  // https://nolebase-integrations.ayaka.io/pages/zh-CN/integrations/vitepress-plugin-git-changelog/
  // vite: {
  //   plugins: [
  //     GitChangelog({
  //       repoURL: () => 'https://github.com/GoldenPotato137/PotatoVN.Doc',
  //     }),
  //     GitChangelogMarkdownSection(),
  //   ],
  // },
  
  title: "PotatoVN",
  description: "PotatoVN Official Website",
  head: [
    ['link', {rel: 'icon', href: '/favicon-16x16.png', sizes:'16x16'}],
    ['link', {rel: 'icon', href: '/favicon-32x32.png', sizes:'32x32'}],
  ],
  lang: 'zh-CN',
  lastUpdated: true,
  markdown: {
    math: true,
    container: {
      tipLabel: '提示',
      warningLabel: '警告',
      dangerLabel: '危险',
      infoLabel: '信息',
      detailsLabel: '详细信息',
      noteLabel: '为什么',
    },
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: "/avatar.png",
    nav: [
      { text: '主页', link: '/' },
      { text: '使用指北', link: '/usage/how-to-use/brief' },
      { text: '一起开发', link: '/development' },
      { text: '更新日志', link: '/upgrade-log' },
    ],
    search: { provider: 'local' },
    sidebar: SideBar,
    socialLinks: [
      { icon: 'github', link: 'https://github.com/GoldenPotato137/PotatoVN' }
    ],
    editLink: {
      pattern: 'https://pr.new/GoldenPotato137/PotatoVN.Doc/edit/stackblitz/:path',
      text: '编辑本页面',
    },
    docFooter: {
      prev: '上一页',
      next: '下一页',
    },
    footer:{
      message: '<a href="https://beian.miit.gov.cn/">桂ICP备20002051号-2</a>',
      copyright: 'Power by <a href="https://vitepress.dev/">VitePress</a>  |  Copyright © 2024 PotatoVN.net  | <a href="https://github.com/GoldenPotato137/PotatoVN?tab=Apache-2.0-1-ov-file#readme">Apache2 License</a>',
    }
  }
})

