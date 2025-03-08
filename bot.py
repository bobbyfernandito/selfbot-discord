import discord
from discord.ext import commands
import random
import asyncio

# Inisialisasi bot
bot = commands.Bot(command_prefix='!', self_bot=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(int(CHANNEL_ID))  
    
    while True:
        message = random.choice(messages)
        await channel.send(message)
        await asyncio.sleep(random.randint(MIN_DELAY, MAX_DELAY))  

def welcome_message():
    print("\033[1;34m" + "="*50 + "\033[0m")  
    print("\033[1;32mSelamat Datang di Bot OhDearBobby!\033[0m")  
    print("\033[1;33mCreated by: OhDeerBobby \033[0m")  
    print("\033[1;36mSiap mengirim pesan otomatis ke Discord!\033[0m")  
    print("\033[1;34m" + "="*50 + "\033[0m")  
    print("Silakan masukkan konfigurasi di bawah ini:\n")

def get_config():
    global TOKEN, CHANNEL_ID, messages, MIN_DELAY, MAX_DELAY
    
    welcome_message()
    
    TOKEN = input("\033[1;35mMasukkan TOKEN bot Anda: \033[0m")
    
    CHANNEL_ID = input("\033[1;35mMasukkan CHANNEL_ID: \033[0m")
    
    print("\033[1;35mMasukkan pesan-pesan yang ingin digunakan (ketik 'SELESAI' untuk mengakhiri):\033[0m")
    messages = []
    while True:
        msg = input("Pesan: ")
        if msg.upper() == 'SELESAI':
            break
        messages.append(msg)
    
    while True:
        try:
            min_delay = float(input("\033[1;35mMasukkan jeda minimum (dalam menit): \033[0m"))
            max_delay = float(input("\033[1;35mMasukkan jeda maksimum (dalam menit): \033[0m"))
            if min_delay <= 0 or max_delay <= 0:
                print("\033[1;31mJeda harus lebih dari 0 menit!\033[0m")
            elif min_delay > max_delay:
                print("\033[1;31mJeda minimum harus lebih kecil atau sama dengan jeda maksimum!\033[0m")
            else:
                MIN_DELAY = int(min_delay * 60)  # Konversi ke detik
                MAX_DELAY = int(max_delay * 60)  # Konversi ke detik
                break
        except ValueError:
            print("\033[1;31mMasukkan angka yang valid!\033[0m")
    
    # Validasi input
    if not TOKEN:
        raise ValueError("TOKEN tidak boleh kosong!")
    if not CHANNEL_ID:
        raise ValueError("CHANNEL_ID tidak boleh kosong!")
    if not messages:
        raise ValueError("Daftar pesan tidak boleh kosong!")
    
    return TOKEN, CHANNEL_ID, messages, MIN_DELAY, MAX_DELAY

# Main execution
if __name__ == "__main__":
    try:
        TOKEN, CHANNEL_ID, messages, MIN_DELAY, MAX_DELAY = get_config()
        
        print("\n\033[1;32mKonfigurasi Berhasil!\033[0m")
        print(f"TOKEN: {'*' * len(TOKEN[:-4]) + TOKEN[-4:]}")
        print(f"CHANNEL_ID: {CHANNEL_ID}")
        print(f"Pesan: {messages}")
        print(f"Jeda: {MIN_DELAY//60}-{MAX_DELAY//60} menit")
        print("\033[1;34m" + "="*50 + "\033[0m")
        
        # Jalankan bot
        bot.run(TOKEN)
        
    except ValueError as e:
        print(f"\033[1;31mError: {e}\033[0m")
    except Exception as e:
        print(f"\033[1;31mTerjadi kesalahan: {e}\033[0m")
