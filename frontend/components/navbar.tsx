"use client";

import { Profile } from "./profile"
import { LoginModal } from "./loginModal"
import { useSession } from "next-auth/react";


export  function Navbar(){
     const { data: session, status } = useSession();
     const isLoading = status === "loading"

 

 


    return (
        <div className="navbar bg-base-100 shadow-sm">
  <div className="navbar-start">
    
    <a className="btn btn-ghost text-xl" href="/">SummerizeClub</a>
  </div>
  <div className="navbar-end flex">
    <div className="navbar-end">
    {
      isLoading? (<span className="loading loading-spinner loading-md"/>) :
      session? <Profile session={session} /> : <LoginModal/>
    
    }
  </div>
    
  </div>
  
</div>
    )
}