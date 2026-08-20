import { useState } from 'react'
import {useCallback,useEffect,useRef} from "react"

function App() {
  const [length,setLength]=useState(8)
  const [numberAllowed,setNumberAllowed]=useState(false)
  const[characterAllowed,setCharacterAllowed]=useState(false)
  const [password,setPassword]=useState("")
  //useref hook
  const passwordRef=useRef(null)
  const passwordGenerator=useCallback(()=>{
   let pass=""
   let str="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 
   if(numberAllowed){
    str=str+"0123456789"

   }
  if(characterAllowed){
    str=str+"!@#$%^&*-_+=[]{}~`/<>"
  }
  for(let i=1; i<=length;i++){
    let char=Math.floor(Math.random()*str.length+1)
    pass+=str.charAt(char)
    setPassword(pass)
  }
  },[length,numberAllowed,characterAllowed])
  const copyPasswordtoClipboard=useCallback(()=>{
    passwordRef.current?.select()
    passwordRef.current?.setSelectionRange(0,password.length)
    window.navigator.clipboard.writeText(password)
  },[password])
useEffect(()=>{passwordGenerator()},[length,numberAllowed,characterAllowed,passwordGenerator])
  

  return (
    <>
     
      <div className="w-full max-w-md mx-auto shadow-md rounded-lg px-4 my-8  bg-gray-800">
         <h1 className="text-4xl text-center text-white my-3">Password Genrator</h1>
        <div className="flex shadow rounded-lg overflow-hidden mb-4 bg-white text-black-500">
          <input
          type="text"
          value={password}
          className="outline-none w-full py-1 px-3 text-black-700"
          placeholder='Password'
          readOnly
          ref={passwordRef}
          />
         < button className="outline-none bg-blue-700 text-white px-4 py-0.5 shrink-0" onClick={copyPasswordtoClipboard}>Copy</button>
        </div>
        <div className="flex text-sm gap-x-2">
          <div className="flex items-center gap-x-1"></div>
          <input type="range" min={6} max={100} value={length} className="cursor-pointer" onChange={(e)=>{setLength(e.target.value)}} />
          <label className='text-orange-600'>Length:{length}</label>
        </div>
        <div className="flex items-center gap-x-1">
          <input 
          type="checkbox"
          defaultChecked={numberAllowed}
          id="numberInput"
          onChange={()=>{
            setNumberAllowed((prev)=>!prev);
          }}
          />
          <label htmlFor="numInput">Numbers</label>
        </div>
        <div className="flex items-center gap-x-1">
          <input
          type="checkbox"
          defaultChecked={characterAllowed}
          id="characterInput"
          onChange={()=>{
            setCharacterAllowed((prev)=>!prev);
          }}
          />
          <label htmlFor="characterInput">Characters</label>
        </div>
        

      </div>
    </>
  )
}

export default App;
