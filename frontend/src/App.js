import { Route, Routes } from "react-router-dom";
import SignIn from "./components/SignIn";
import SignUp from "./components/SignUp";
import Layout from "./components/Layout";
import CreateCompany from "./components/CreateCompany";
import RequireAuth from "./components/RequireAuth";
import Dashboard from "./pages/Dashboard";
import Page404 from "./components/ErrorPages/Page404";
import ComingSoon from "./components/ErrorPages/ComingSoon";
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
        <Route path="/page404" element={<Page404 />} />
        <Route path="/comingsoon" element={<ComingSoon />} />
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
