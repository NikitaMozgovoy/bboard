import logo from './logo.svg';
import React, {useState, useEffect} from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [bb, setBb] = useState([])

  useEffect(()=>{
    axios({
      method:'GET',
      url:'http://127.0.0.1:8000/api/bboard'
    }).then(response => {
      setBb(response.data)
    })
  }, [])
  return (
    <div className="App">
      <ul>
        {bb.map(bb => (
          <>
          <p>{bb.title}</p>
          <img src = {bb.image}></img>
          <p>{bb.price}</p>
          <p>{bb.content}</p>
          </>
        ))}
      </ul>

    </div>
  );
}

export default App;
