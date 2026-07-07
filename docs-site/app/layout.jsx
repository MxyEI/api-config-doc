import { Layout, Navbar, Footer } from 'nextra-theme-docs'
import { Head } from 'nextra/components'
import { getPageMap } from 'nextra/page-map'
import 'nextra-theme-docs/style.css'
import './globals.css'
import config from '../site-config.mjs'
const BARE = process.env.BARE_LAYOUT === '1'

export const metadata = {
  title: {
    default: `${config.siteName} Docs`,
    template: `%s | ${config.siteName} Docs`
  },
  description: config.description
}

export default async function RootLayout({ children }) {
  return (
    <html lang="zh" dir="ltr" suppressHydrationWarning>
      {/* 主题参数与 hao.ai 一致: 主色蓝 hue 212°/204°, 内容宽 90rem（见 globals.css） */}
      <Head />
      <body>
        {BARE ? children : <Layout
          navbar={
            <Navbar
              logo={<b style={{ fontSize: '1.1em' }}>{config.siteName}</b>}
              projectLink={config.siteUrl}
            />
          }
          pageMap={await getPageMap()}
          footer={<Footer>© {config.siteName}</Footer>}
        >
          {children}
        </Layout>}
      </body>
    </html>
  )
}
