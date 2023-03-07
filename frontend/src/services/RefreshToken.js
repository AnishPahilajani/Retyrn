export async function RefreshToken(setAuth) {
  let resp = await fetch("http://localhost:8000/refresh", {
    method: "GET",
    headers: {
      "Content-type": "application/json",
    },
  });
  let data = await resp.json();
  if (resp.status === 200) {
    setAuth((prev) => {
      return { ...prev, accessToken: data.access_token };
    });
  }
  return data.access_token;
}
