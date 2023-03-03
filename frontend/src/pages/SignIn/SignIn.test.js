import { render, fireEvent } from "@testing-library/react";
import { act } from "react-dom/test-utils";
import SignIn from "./SignIn";

describe("Signin", () => {
  describe("with valid inputs", () => {
    test("calls the onSubmit function", async () => {
      const mockOnSubmit = jest.fn();
      const { getByLabelText, getByRole } = render(
        <SignIn onSubmit={mockOnSubmit} />
      );
      await act(async () => {
        fireEvent.change(getByLabelText("Email Address *"), {
          target: { value: "email@test.com" },
        });
        fireEvent.change(getByLabelText("Password *"), {
          target: { value: "1234567" },
        });
      });
      await act(async () => {
        fireEvent.click(getByRole("button"));
      });
      expect(mockOnSubmit).toHaveBeenCalled();
    });
  });
});
