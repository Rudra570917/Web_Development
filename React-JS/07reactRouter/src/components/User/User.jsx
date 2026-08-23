import React from 'react'
import { useParams } from 'react-router-dom'

function User() {
    const {userid} = useParams()
  return (
    <div className='bg-amber-600 text-black-600 text-3xl font-bolder p-4 m-6 text-center'>User: {userid}</div>
  )
}

export default User