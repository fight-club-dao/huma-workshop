import { ChainEnum } from './chain'
import BASE_POOL_CONFIG_ABI from '../abis/BasePoolConfig.json'
import BASE_CREDIT_POOL_ABI from '../abis/BaseCreditPool.json'
import HDT_ABI from '../abis/HDT.json'
import { IconType } from '../utilTypes'
import { UsdcIcon } from '../components/icons'

export enum POOL_NAME {
  HumaCreditLine = 'HumaCreditLine',
}

export enum POOL_TYPE {
  CreditLine = 'CreditLine',
}

export type PoolMapType = {
  [poolType in POOL_TYPE]: {
    [poolName: string]: {
      name: string
      borrowDesc: string
      lendDesc: string
    }
  }
}

export type PoolInfoType = {
  basePoolConfig: string
  pool: string
  poolFeeManager: string
  poolUnderlyingToken: {
    address: string
    symbol: string
    decimals: number
    icon: IconType
  }
  assetAddress?: string
  poolName: POOL_NAME
  poolType: POOL_TYPE
  poolAbi: unknown
  basePoolConfigAbi: unknown
  HDT: {
    address: string
    abi: unknown
  }
}

export type PoolContractMapType = {
  [chainId: number]: {
    [POOL_TYPE.CreditLine]: {
      [poolName: string]: PoolInfoType
    }
  }
}

export const PoolMap: PoolMapType = {
  [POOL_TYPE.CreditLine]: {
    [POOL_NAME.HumaCreditLine]: {
      name: 'Huma Credit Line',
      borrowDesc:
        'Credit lines backed by your future crypto income. Only available to the members of partner DAOs during beta.',
      lendDesc:
        'Earn active yield by participating in credit lines backed by on-chain income. Only available to the members of partner DAOs during beta.',
    },
  },
}

export const PoolContractMap: PoolContractMapType = {
  [ChainEnum.Goerli]: {
    [POOL_TYPE.CreditLine]: {
      [POOL_NAME.HumaCreditLine]: {
        basePoolConfig: '0x55a4Bf5394DB361e66FCb097BBcac89D415941E8', // TODO: Replace this with the BaseCreditPoolConfig contract address
        pool: '0xE42C3ac195DE958B38c323DD14a47894AB7c422c', // TODO: Replace this with the BaseCreditPool contract address
        poolFeeManager: '0x107eB0e06c87D50B69E4a6229bc9Ad31f14a2be5', // TODO: Replace this with the BaseCreditPoolFeeManager contract address
        poolUnderlyingToken: {
          address: '0x0d95acdFE7f4e3c2514A0379A3c461719697c72C', // TODO: Replace this with the USDC contract address
          symbol: 'USDC',
          decimals: 6,
          icon: UsdcIcon,
        },
        poolName: POOL_NAME.HumaCreditLine,
        poolType: POOL_TYPE.CreditLine,
        poolAbi: BASE_CREDIT_POOL_ABI,
        basePoolConfigAbi: BASE_POOL_CONFIG_ABI,
        HDT: {
          address: '0x2770769992268638370fd3FF43b84f245eb6a288', // TODO: Replace this with the BaseCreditHDT contract address
          abi: HDT_ABI,
        },
      },
    },
  },
}
