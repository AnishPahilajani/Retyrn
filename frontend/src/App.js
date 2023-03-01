import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import CreateCompany from "./pages/CreateCompany/CreateCompany.js";
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/create-company" element={<CreateCompany />} />
      </Routes>
    </Router>
  );
}

export default App;
