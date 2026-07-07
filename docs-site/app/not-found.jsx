import { NotFoundPage } from 'nextra-theme-docs'

// Nextra 4 + output:'export' 需要显式的 404 页面，否则静态导出会在
// 预渲染 /_not-found 时报错（缺少主题上下文）。
export default function NotFound() {
  return <NotFoundPage content="返回首页">页面不存在</NotFoundPage>
}
