import { useState } from 'react'
import React from 'react';
import LabeledInput from './LabeledInput';
import StyledButton from './StyledButton';
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <header><h1>Simple Phone Book</h1></header>

      <div>
        <h2>Add Contact</h2>
        <form action="" method="post">
          <LabeledInput label="Name:" type="text" id="name" name="name" />
          <LabeledInput label="Contact:" type="text" id="contact" name="contact_num" />
          <StyledButton type="submit">Add Contact</StyledButton>
        </form>
      </div>

      <div>
        <h2>Search Number</h2>
        <form action="" method="post">
          <LabeledInput label="Name:" type="text" id="name" name="name" />
          <StyledButton type="submit">Search Contact</StyledButton>
        </form>
      </div>
      
      <footer>
        <p className="read-the-docs">
          This is a simple phone book that has 2 functionalities. 
          <ol>
            <li>Add a contact in the phone book.</li>
            <li>Search for the contact by the name of the Person</li>
          </ol>

        </p>
      </footer>
      
    </>
  )
}

export default App
