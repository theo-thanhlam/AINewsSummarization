import { getServerSession } from "next-auth";
import { authOptions } from "@/libs/auth";
import { NextResponse } from "next/server";
import { prisma } from "@/libs/prisma";


export async function DELETE(req: Request) {
    const session = await getServerSession(authOptions);
    if (!session?.user?.email) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }
    const user = await prisma.subscribers.findFirst({
        where:{email:session?.user?.email}

    })
    if (!user){
        return NextResponse.json({ error: "User not found" }, { status: 404 });

    }
    await prisma.subscribers.delete({
        where:{
            id:user.id
        }
    })
    return NextResponse.json({
        message:"User Deleted"
    },{status:200})

}