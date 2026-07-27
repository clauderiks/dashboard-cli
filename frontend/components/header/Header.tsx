export default function Header() {
  return (
    <header style={{
      height:"56px",
      borderBottom:"1px solid #1e293b",
      display:"flex",
      alignItems:"center",
      justifyContent:"space-between",
      padding:"0 16px",
      background:"#020617",
      color:"#fff"
    }}>
      <b>SandboxCode</b>
      <div>Run | Build | Deploy</div>
    </header>
  )
}
