import configUtil from '../utils/config'
import request from '../utils/request'
import timeUtil from '../utils/time'

export type EAPayloadType = {
  poolAddress: string
  borrowerWalletAddress?: string
  receivableAddress?: string
  receivableParam?: string
}

export type ApproveInfoType = {
  aprInBps: number
  creditLimit: number
  intervalInDays: number
  receivableAmount: number
  receivableAsset: string
  receivableParam: number | string
  remainingPeriods: number
  tokenDecimal: number
  tokenName: string
  tokenSymbol: string
}

const approve = async (
  payload: EAPayloadType,
  chainId: number,
  checkIsApproved?: () => Promise<boolean>,
) => {
  const EARejectErrorMessage =
    'Based on your wallet transaction history your application was not approved.'

  try {
    const { data } = await request.post(
      `${configUtil.getEAVerseUrl()}/underwrite`,
      payload,
    )
    const applicationRejectedError = new Error(EARejectErrorMessage, {
      cause: { applicationRejected: true },
    })
    if (data.statusCode >= 500) {
      throw applicationRejectedError
    } else if (data.status) {
      throw applicationRejectedError
    } else if (data.rejectionReason?.length) {
      throw applicationRejectedError
    }

    // @TODO: Make the EA service to make sure the transaction is confirmed
    if (checkIsApproved) {
      // eslint-disable-next-line no-plusplus
      for (let i = 0; i < 120; i++) {
        // eslint-disable-next-line no-await-in-loop
        const isApproved = await checkIsApproved()
        if (isApproved) {
          break
        } else {
          // eslint-disable-next-line no-await-in-loop
          await timeUtil.sleep(1000)
        }
      }
    }

    return data as ApproveInfoType

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
  } catch (error: any) {
    console.error(error)
    throw new Error(error.message ?? EARejectErrorMessage, {
      cause: error.cause,
    })
  }
}

const EAService = {
  approve,
}
export default EAService
