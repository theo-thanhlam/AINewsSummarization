"use client";
import { useSession } from "next-auth/react";
import {  signOut } from 'next-auth/react';

export default function ProfilePage(){
     const { data: session } = useSession();
     async function handleDelete() {
    if (!session?.user?.email) return;

    const res = await fetch("/api/profiles", {
      method: "DELETE",
      headers: { "Content-Type": "application/json" }
      
    });

    if (res.status == 200){
        signOut()

    }

    
  }
    return(
        <div>
            <button onClick={handleDelete} className="btn bg-red-500 text-white">
      Unsubscribe
    </button>
        </div>
    )
}