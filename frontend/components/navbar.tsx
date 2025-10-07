"use client";

import { Profile } from "./profile"
import { LoginModal } from "./loginModal"
import { useSession } from "next-auth/react";


export  function Navbar(){
     const { data: session, status } = useSession();

  if (status === "loading") {
    return (
      <span className="loading loading-spinner loading-md"/>

    )
  }

 


    return (
        <div className="navbar bg-base-100 shadow-sm">
  <div className="navbar-start">
    
    <a className="btn btn-ghost text-xl">SummerizeClub</a>
  </div>
  <div className="navbar-end flex">
    <div className="navbar-end">
    {session? <Profile session={session} /> : <LoginModal/>}
  </div>
    
  </div>
  
</div>
    )
}