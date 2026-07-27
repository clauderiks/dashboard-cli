import Sidebar from "../sidebar/Sidebar";
import Header from "../header/Header";

/**
 * Renders the dashboard layout with a sidebar, header, and centered IDE content area.
 */
export default function Dashboard() {
  return (
    <div style={{
      display:"grid",
      gridTemplateColumns:"260px 1fr",
      height:"100vh"
    }}>
      <Sidebar/>
      <div style={{
        display:"flex",
        flexDirection:"column"
      }}>
        <Header/>
        <main style={{
          flex:1,
          display:"flex",
          alignItems:"center",
          justifyContent:"center",
          background:"#0b1220",
          color:"#fff"
        }}>
          SandboxCode IDE
        </main>
      </div>
    </div>
  );
}
