import { Route, Routes } from "react-router-dom";
import SignIn from "./pages/SignIn";
import SignUp from "./pages/SignUp";
import Layout from "./components/Layout";
import CreateCompany from "./pages/CreateCompany";
import RequireAuth from "./components/RequireAuth";
import Dashboard from "./pages/Dashboard";
const ROLES = {
  User: 1,
  Trucker: 2,
  Admin: 3,
  Company: 4,
};
function App() {
  return (
    <Routes>
      <Route exact path="/" element={<Layout />}>
        {/* public routes */}
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />

        {/* protected routes */}
        <Route element={<RequireAuth />}>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/createcompany" element={<CreateCompany />} />
        </Route>

        <Route element={<RequireAuth allowedRoles={[ROLES.User]} />}></Route>
        <Route element={<RequireAuth allowedRoles={[ROLES.Trucker]} />}></Route>
        <Route element={<RequireAuth allowedRoles={[ROLES.Admin]} />}></Route>
        <Route element={<RequireAuth allowedRoles={[ROLES.Company]} />}></Route>
        {/* catch all */}
      </Route>
    </Routes>
  );
}

export default App;
