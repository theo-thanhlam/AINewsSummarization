'use server'
import Image from "next/image";
import { Navbar } from "@/components/navbar";
import { Hero } from "@/components/hero";


export default async function Home() {

  return (
    <div className="min-h-screen flex flex-col bg-base-100 text-base-content">
        <Hero />
      
    </div>
  );
}
