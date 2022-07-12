import React, { useContext } from "react";
import { Context } from "..";
import Mybutton from "../UI/buttons/MyButton";
import Myloader from "../UI/Loader/ Myloader";

const HomePage = () => {

  
  const { store } = useContext(Context);


  return (
    <div className="post">

      <h1>Hello {localStorage.getItem('email')}</h1>
      {store.isAuth &&
        <h1>Role: {store.userRole}</h1>

      }
    
    </div>
  );
};

export default HomePage;
