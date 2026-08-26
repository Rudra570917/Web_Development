import { useState } from 'react'
import AddTodo from './components/AddTodo'
import Todos from './components/Todos'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <h1 className="text-6xl text-center bg-orange-600 p-4 ">Learn about redux toolkit</h1>
     <AddTodo/>
     <Todos/>
    </>
  )
}

export default App
