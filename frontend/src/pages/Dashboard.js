import React from "react";

import useAuth from "../hooks/useAuth";
import useLogout from "../hooks/useLogout";
import { Link, useNavigate } from "react-router-dom";
const Dashboard = () => {
  const navigate = useNavigate();
  // const logout = useLogout();
  // const signOut = async () => {
  //   await logout();
  //   navigate("/");
  // };
  return (
    <div>
      <Link to="../createcompany">Create Company</Link>
      Dashboard
      {/* <form onSubmit={signOut}>
        <button>Logout</button>
      </form> */}
    </div>
  );
};

export default Dashboard;
