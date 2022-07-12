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
  return (
    <div>
      <Myinput
        onChange={(e) => setEmail(e.target.value)}
        value={email}
        type="text"
        placeholder="Email"
      />
      <Myinput
        onChange={(e) => setPassword(e.target.value)}
        value={password}
        type="password"
        placeholder="Password"
      />
      <Mybutton onClick={() => store.login(email, password)}>Login</Mybutton>
    </div>
  );
};

export default observer(LoginForm);
