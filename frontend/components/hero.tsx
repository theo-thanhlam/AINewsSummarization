"use client"
import { useSession } from "next-auth/react";
export function Hero(){
  const {data:session} = useSession()


    const openLogin = () => {
    const modal = document.getElementById("login_modal") as HTMLDialogElement;
    modal?.showModal();
  };

  
    return (
        <div className="min-h-screen flex flex-col bg-base-100 text-base-content">
            <section className="hero min-h-[80vh] bg-base-100">
            <div className="hero-content text-center flex flex-col">
              <h1 className="text-4xl md:text-6xl font-bold mb-4">
                Stay Informed. Save Time.
              </h1>
              <p className="text-lg md:text-xl mb-6 max-w-md mx-auto">
                Get concise, AI-powered news summaries delivered to your inbox every morning.
              </p>

              {!session ?  <button className="btn btn-primary" onClick={openLogin}>
       Subscribe Now
      </button> : <button className="btn btn-primary" ><a href="/profile">Manage your preferences</a></button>}
             
              
            </div>
          </section>
          
          
        </div>
      );
}