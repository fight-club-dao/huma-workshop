import React from 'react'

import { LoadingModal } from '../../../components'

export function CheckingEA(): React.ReactElement | null {
  return (
    <LoadingModal
      title='Approval Pending'
      description='Waiting for approval confirmation...'
    />
  )
}
