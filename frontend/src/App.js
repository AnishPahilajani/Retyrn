import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import CreateCompany from "./pages/CreateCompany/CreateCompany";
function App() {
  return (
    <Router>
      <Routes>
        {/* <Route exact path="/" element={<Home />} /> */}
        <Route path="/create-company" element={<CreateCompany />} />
      </Routes>
    </Router>
  );
}

export default App;
