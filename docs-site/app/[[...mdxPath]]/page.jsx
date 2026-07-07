import { generateStaticParamsFor, importPage } from 'nextra/pages'
import { useMDXComponents as getMDXComponents } from '../../mdx-components'

export const generateStaticParams = generateStaticParamsFor('mdxPath')

export async function generateMetadata(props) {
  const params = await props.params
  const { metadata } = await importPage(params.mdxPath)
  return metadata
}

const Wrapper = getMDXComponents().wrapper

export default async function Page(props) {
  const params = await props.params
  let result
  try {
    result = await importPage(params.mdxPath)
  } catch (e) {
    console.error('IMPORT_FAIL', params.mdxPath, e && e.stack)
    throw e
  }
  const { default: MDXContent, toc, metadata } = result
  let child
  try {
    child = MDXContent({ ...props, params })
  } catch (e) {
    console.error('MDX_RENDER_FAIL', params.mdxPath, e && e.stack)
    throw e
  }
  try {
    return (
      <Wrapper toc={toc} metadata={metadata}>
        {child}
      </Wrapper>
    )
  } catch (e) {
    console.error('WRAPPER_FAIL', params.mdxPath, e && e.stack)
    throw e
  }
}
