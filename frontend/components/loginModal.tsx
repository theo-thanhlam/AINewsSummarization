"use client";
import { useRef } from "react";
import { LoginForm } from "./loginForm"; 

export function LoginModal() {
  const modalRef = useRef<HTMLDialogElement>(null);

  const openModal = () => {
    modalRef.current?.showModal();
  };

  return (
    <div className="flex justify-center">
      {/* Button to open modal */}
      <button className="btn btn-primary rounded" onClick={openModal}>
        Login
      </button>

      {/* DaisyUI Modal */}
      <dialog ref={modalRef} className="modal modal-middle" id="login_modal">
        <div className="modal-box relative max-w-md w-full bg-amber-50 rounded">
          {/* ✕ Close button */}
          <form method="dialog">
            <button className="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">
              ✕
            </button>
          </form>

          {/* Title */}
          <h3 className="font-bold text-lg mb-4 text-center">Log In / Sign Up</h3>

          {/* Login Form component */}
          <LoginForm />


      
        </div>

        {/* Clicking outside closes modal */}
        <form method="dialog" className="modal-backdrop">
          <button>close</button>
        </form>
      </dialog>
    </div>
  );
}
