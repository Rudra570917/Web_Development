import React from 'react'
import image from '../assets/hero.png'
export default function Card({ children, channel }) {
  return (
    <div className="flex flex-col items-center p-7 rounded-2xl">
      <div>
        <img className="size-48 shadow-xl rounded-md" alt="Image" src={image} />
      </div>
      <div className="flex">
        <span className="text-2xl font-medium">Class Warfare</span>
        <span className="font-medium text-sky-500">{channel}</span>
        <span className="flex gap-2 font-medium text-gray-600 dark:text-gray-400">
          <span>No. 4</span>
          <span>·</span>
          <span>2025</span>
        </span>
      </div>
    </div>
  )
}
