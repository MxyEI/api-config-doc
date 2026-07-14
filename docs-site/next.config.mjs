import nextra from 'nextra'

const withNextra = nextra({
  defaultShowCopyCode: true,
  search: false
})

export default withNextra({
  output: 'export',
  // 站点挂载在 api.look2eye.com/tutorial/ 子路径下（Caddy file_server），
  // 改这里的同时要同步改 Caddy 的 /tutorial 路由前缀
  basePath: '/tutorial',
  trailingSlash: true,
  images: { unoptimized: true }
})
