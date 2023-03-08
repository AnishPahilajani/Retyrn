export async function NewCompany(values, navigate) {
  console.log(values);
  try {
    let resp = await fetch("http://localhost:8000/company", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(values),
    });
    let data = await resp.json();

    navigate("../comingsoon");
  } catch (err) {
    navigate("../comingsoon");
  }
}
