import React from "react";
import "./CreateCompany.css";
const CreateCompany = () => {
  return (
    <div className="CCScreenContainer">
      <div id="CCTitle">
        <div>Create</div>
        <div>Company</div>
      </div>
      <div className="CCFormContainer">
        <form>
          <div className="CCInputField">
            <div className="CCInputLabels">Type of Company</div>
            <select className="CCInputFields" required>
              <option></option>
              <option value="Trucking">Trucking</option>
            </select>
          </div>
          <div className="CCInputField">
            <div className="CCInputLabels">Company Name</div>
            <input
              className="CCInputFields"
              type="text"
              placeholder="Retyrn Corporation"
              required
            ></input>
          </div>
          <div className="CCInputField">
            <div className="CCInputLabels">Company Address</div>
            <input
              className="CCInputFields"
              type="text"
              placeholder="1600 Pennsylvania Avenue NW, Washington, DC 20500"
              required
            ></input>
          </div>
          <div className="CCInputField">
            <div className="CCInputLabels">Company Phone Number</div>
            <input
              className="CCInputFields"
              type="text"
              placeholder="123-456-7890"
              required
            ></input>
          </div>
          <div className="CCInputField">
            <div className="CCInputLabels">Owner Name</div>
            <input
              className="CCInputFields"
              type="text"
              placeholder="John Smith"
              required
            ></input>
          </div>
          <div id="CCButtonContainer">
            <button className="CCButtons" id="CCCancelButton">
              Cancel
            </button>
            <button className="CCButtons" id="CCSaveButton">
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CreateCompany;
