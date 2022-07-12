import { useContext, useEffect, useState } from "react";
import LoginForm from "./components/LoginForm";
import RegistrationForm from "./components/RegistrationFrom";
import HomePage from "./pages/home";
import WorkerList from "./pages/workerList";
import { Routes, Route, Link } from "react-router-dom";
import Paginator from "./UI/paginator/paginator";
import "./styles/App.css";
import Register from "./pages/register";
import Login from "./pages/login";
import { Context } from ".";
import { observer } from "mobx-react-lite";
import Mybutton from "./UI/buttons/MyButton";
import NotAuthPaginator from "./UI/paginator/notAuth_paginator";
import WorkerItem from "./components/workerItem";
import WorkerDetail from "./components/workerDetail";
import UserAppointment from "./pages/userAppointment";
import WorkerAppointment from "./pages/workerAppointment";
import Myloader from "./UI/Loader/ Myloader";

function App() {
  const [page, setPage] = useState("");
  const changePage = (page) => {
    setPage(page);
  };
  const { store } = useContext(Context);

  useEffect(() => {
    if (localStorage.getItem("tokenAccess")) {
      store.checkAuth();
    }
  }, []);

  if (store.isLoading) {
    return (
      <div className="users__wrapper">
        <div className="users">
          <div className="loaderError__container">
            <Myloader />
          </div>
        </div>
      </div>
    );
  }

  if (!store.isAuth) {
    return (
      <div>
        <header>
          <NotAuthPaginator page={page} changePage={changePage} />
        </header>
        <Routes>
          <Route path="/home" element={<HomePage />} />
          <Route path="/*" element={<HomePage />} />
          <Route path="/registration" element={<Register />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    );
  }
  if (store.userRole === "CUSTOMER") {
    return (
      <div>
        <header>
          <div className="navbar__header">
            <Paginator
              page={page}
              changePage={changePage}
              role={store.userRole}
            />

            <Mybutton onClick={() => store.logout()}>
              <h2>Logout</h2>
            </Mybutton>
          </div>
        </header>

        <Routes>
          <Route path="/home" element={<HomePage />} />
          <Route path="/workerList" element={<WorkerList />} />
          <Route path="/userAppointment" element={<UserAppointment />} />
          <Route path="/*" element={<HomePage />} />
          <Route path="/workers/:workerId" element={<WorkerDetail />} />
        </Routes>
      </div>
    );
  }
  if (!store.isLoading) {
    return (
      <div>
        <header>
          <div className="navbar__header">
            <Paginator page={page} changePage={changePage} />

            <Mybutton onClick={() => store.logout()}>
              <h2>Logout</h2>
            </Mybutton>
          </div>
        </header>

        <Routes>
          <Route
            path="/home"
            element={<HomePage />}
            userRole={store.userRole}
          />
          {/* <Route path="/workerList" element={<WorkerList />} /> */}
          <Route path="/workerAppointment" element={<WorkerAppointment />} />
          <Route path="/*" element={<HomePage />} />
          {/* <Route path="/workers/:workerId" element={<WorkerDetail/>}/> */}
        </Routes>
      </div>
    );
  }
}

export default observer(App);
