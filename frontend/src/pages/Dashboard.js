import React from "react";

import useAuth from "../hooks/useAuth";
import useLogout from "../hooks/useLogout";
import { Navigate } from "react-router-dom";
import { Link } from "react-router-dom";
const Dashboard = () => {
  const { auth } = useAuth();
  // console.log(auth.accessToken);
  // const logout = useLogout();
  // const signOut = async () => {
  //   await logout();
  //   navigate("/");
  // };
  return (
    <div>
      <div>
        <Link to="../createcompany">Create Company</Link>
        Dashboard
        {/* <form onSubmit={signOut}>
        <button>Logout</button>
      </form> */}
      </div>
    </div>
  );
};

export default Dashboard;
