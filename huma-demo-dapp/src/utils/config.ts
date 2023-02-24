import { CHAINS } from './chain'

const getDevPrefix = () =>
  process.env.REACT_APP_FORCE_DEV_PREFIX_FOR_URLS ||
  window.location.hostname.startsWith('dev')
    ? 'dev.'
    : ''

const getEAVerseUrl = (chainId: number) => {
  if (process.env.REACT_APP_EA_BASE_URL) {
    return process.env.REACT_APP_EA_BASE_URL
  }

  const network = CHAINS[chainId].name
  return `https://${getDevPrefix()}${network}.eaverse.huma.finance`
}
const getEABaseUrlV1 = (chainId: number) => {
  const network = CHAINS[chainId].name
  return `https://${network}.risk.huma.finance`
}

const configUtil = {
  getEAVerseUrl,
  getEABaseUrlV1,
}

export default configUtil
