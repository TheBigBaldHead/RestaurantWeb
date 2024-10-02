import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="text-center">
      <h1 className="text-4xl font-bold text-blue-500">
        Hello, Tailwind in React!
      </h1>
    </div>
  );
}

export default App;
