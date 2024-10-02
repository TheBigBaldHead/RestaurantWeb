import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import "./custom_styles.css";
import { useBearStore } from "./store/store";

function App() {
  const [count, setCount] = useState(0);
  const bears = useBearStore((state) => state.bears);
  const increasePopulation = useBearStore((state) => state.increasePopulation);

  return (
    <div className="card text-center w-1/2 mx-auto">
      <h1 className="text-4xl font-bold text-blue-500">
        Hello, Tailwind in React!
      </h1>
      <h1>{bears} bears around here ...</h1>
      <button
        class="bg-red-700 rounded-2xl w-10"
        onClick={() => increasePopulation()}
      >
        +
      </button>
    </div>
  );
}

export default App;
