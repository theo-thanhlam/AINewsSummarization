'use client';
import {  signOut } from 'next-auth/react';

interface props{
  session:any
}


export function Profile({session}:props){
    const handleSignout = async () => {
      signOut()
    }
  
    return (
        <div className="dropdown dropdown-end">
      <div tabIndex={0} role="button" className="btn btn-ghost btn-circle avatar">
        <div className="w-10 rounded-full">
          <img
            alt="Profile Image"
            src={session?.user?.image} />
        </div>
      </div>
      <ul
        tabIndex={0}
        className="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow">
        <li>Hello {session.user.name}</li>
        <hr/>
        <li><button onClick={handleSignout}>Logout</button></li>
      </ul>
    </div>
    )
}