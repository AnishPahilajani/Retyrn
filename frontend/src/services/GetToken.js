export async function GetToken(url, values, setErrMsg, setAuth, navigate) {
  try {
    let resp = await fetch("http://localhost:8000/" + url, {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(values),
    });
    let data = await resp.json();

    if (resp.status === 200 || resp.status === 201) {
      const accessToken = data?.access_token;
      const roles = data?.roles;
      setAuth({ roles, accessToken });
      navigate("../dashboard");
    } else {
      setErrMsg(data.detail);
    }
  } catch (err) {
    // setErrMsg("No Server Response");
    if (!err.response) {
      setErrMsg("No Server Response");
    } else {
      setErrMsg("Login Failed");
    }
    navigate("../page404");
  }
}
