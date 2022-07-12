import React from "react";
import { useContext } from "react";
import { useState } from "react";
import { Context } from "..";
import { observer } from "mobx-react-lite";
import Myinput from "../UI/inputs/MyInput";
import Mybutton from "../UI/buttons/MyButton";

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { store } = useContext(Context);
  const [error, setError] = useState("")

  const login = (email, password) => {
    store.login(email, password).then((res) => (res)).catch(e => setError(e.response.data))
  }
  return (
    <div>
      {error.password && <div style={{ color: "red" }}>Fill out all fields</div>}
      {error.detail && <div style={{ color: "red" }}>{error.detail}</div>}
      <Myinput
        onChange={(e) => setEmail(e.target.value)}
        value={email}
        type="text"
        placeholder="Email"
      />
      {/* {error.password && <div style={{ color: "red" }}>{error.password[0]}</div>} */}
      <Myinput
        onChange={(e) => setPassword(e.target.value)}
        value={password}
        type="password"
        placeholder="Password"
      />
      <Mybutton onClick={() => login(email, password)}>Login</Mybutton>
    </div>
  );
};

export default observer(LoginForm);
