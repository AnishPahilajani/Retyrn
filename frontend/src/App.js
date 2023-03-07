import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SignIn from "./pages/SignIn/SignIn";
import SignUp from "./pages/SignUp/SignUp";
import CreateCompany from "./pages/CreateCompany/CreateCompany";
import Page404 from "./pages/ErrorPages/Page404";
import ComingSoon from "./pages/ErrorPages/ComingSoon";
function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          {/* <Route exact path="/" element={<Home />} /> */}
          <Route path="/signin" element={<SignIn />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/createcompany" element={<CreateCompany />} />
          <Route path="/page404" element={<Page404 />} />
          <Route path="/comingsoon" element={<ComingSoon />} />
          <Route component={Page404} />
          {/**add switch to route to 404 page when needed */}
        </Routes>
      </Router>
    </div>
  );
}

export default App;

