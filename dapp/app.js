let contract;

const address = "0xD44B8519193667757dF52EE6F50BfDBAa0E7609C";

const abi = [
  "function setMessage(string)",
  "function getMessage() view returns (string)"
];

async function connect() {
  const provider = new ethers.BrowserProvider(window.ethereum);
  const signer = await provider.getSigner();
  contract = new ethers.Contract(address, abi, signer);
}

async function setMsg() {
  const val = document.getElementById("msg").value;
  const tx = await contract.setMessage(val);
  await tx.wait();
  alert("Saved!");
}

async function getMsg() {
  const msg = await contract.getMessage();
  document.getElementById("output").innerText = msg;
}