import React, { createContext } from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import Store from "./store/store";
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));

const store = new Store();

export const Context = createContext({
  store,
});
root.render(
  <BrowserRouter>
    <Context.Provider
      value={{
        store,
      }}
    >
      <App />
    </Context.Provider>
  </BrowserRouter>
);
