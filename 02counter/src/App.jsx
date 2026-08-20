import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [counter,setCounter] = useState(15);
  const addValue = () => {
    console.log("value added",Math.random());
    setCounter(counter + 1);
  }
  const removeValue = () => {
    console.log("value removed",Math.random());
    if(counter > 0){
      setCounter(counter - 1);
    }
  }
 

  return (
    <>
      <h1>React JS</h1>
      <h2>Counter value:{counter}</h2>
      <button onClick={addValue}>Add value</button>
      <br/>
      <button onClick={removeValue} >Remove value</button>
    </>
  )
}

export default App
