import { AuthOptions } from 'next-auth';
import GoogleProvider from 'next-auth/providers/google';
import { prisma } from '@/libs/prisma';

export const authOptions: AuthOptions = {
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID as string,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET as string,
      authorization: {
        params: {
          prompt: "select_account consent",
        }
      }
    }),
  ],
  callbacks: {

    async signIn({ user, account, profile }){
      try {
        // Check if the user exists
        const existingUser = await prisma.subscribers.findFirst({
          where: { email: user.email },
        });

        if (!existingUser) {
          // Create new user
          await prisma.subscribers.create({
            data: {
              
              email: user.email,
              
            },
          });
        }

        return true; // allow sign-in
      } catch (error) {
        console.error("Error checking/creating user:", error);
        return false; // deny sign-in if something goes wrong
      }
    
    },

    async jwt({ token, account, user }) {
      // Persist the OAuth access_token and or the user id to the token right after signin
      if (account?.id_token) {
        token.id_token = account.id_token as string;
      }
      return token;
    },
    async session({ session, token, user }) {
      // Send properties to the client, like an access_token and user id from a provider.
      
      return session;
       
    },
  },
  secret: process.env.NEXTAUTH_SECRET,
  
  
};