import { useLocation, Navigate, Outlet } from "react-router-dom";
import useAuth from "../hooks/useAuth";

const RequireAuth = ({ allowedRoles }) => {
  const { auth } = useAuth();
  const location = useLocation();
  const access_token = localStorage.getItem("token");
  return access_token ? (
    <Outlet />
  ) : (
    <div>
      <Navigate to="/signin" state={{ from: location }} replace />
    </div>
  );
};

export default RequireAuth;
