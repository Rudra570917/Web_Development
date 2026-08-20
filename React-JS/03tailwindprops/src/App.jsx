import { useState } from 'react'
// import image from './assets/react.svg'
import Card from './components/Card'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1 className='text-3xl font-bold underline text-center text-blue-900'>
        Tailwind CSS with React JS
     </h1>
     <Card channel="chaiaurcode"/>
    </>
  )
}

export default App
