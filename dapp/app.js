let contract;

const address = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4";

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