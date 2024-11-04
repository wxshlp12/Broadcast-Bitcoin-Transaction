# DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency

<!-- wp:paragraph -->
<p>There are many tools available on the internet to create fake signature values ​​in Bitcoin cryptocurrency, one of them is&nbsp;<a href="https://github.com/smartibase/Broadcast-Bitcoin-Transaction/tree/main/darksignature"><strong>DarkSignature</strong></a></p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p><em>The basic idea behind&nbsp;<a href="https://github.com/smartibase/Broadcast-Bitcoin-Transaction/tree/main/darksignature"><strong>DarkSignature</strong></a>&nbsp;is that if there are vulnerabilities in cryptographic algorithms such as ECDSA (Elliptic Curve Digital Signature Algorithm), it is possible to generate invalid or fake signatures that will be accepted as valid by the system.</em></p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:image {"id":1250} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image-1.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1250"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>This command changes the current directory to&nbsp;&nbsp;<code>darksignature</code>. This means that all subsequent commands will be executed in this folder. If the necessary scripts or programs for decoding transactions are in it, this will allow them to be used. The command&nbsp;&nbsp;<code>ls</code>&nbsp;lists all files and directories in the current directory (in this case,&nbsp;&nbsp;<code>darksignature</code>). This is useful for checking for files or scripts that may be needed for further actions. By default, the command does not show hidden files (those that begin with a dot).</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>cd darksignature/

ls</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1249} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1249"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>This command changes the permissions of a file or directory&nbsp;&nbsp;darksignature by adding execute permission (&nbsp;<code>+x</code>). This is necessary if you want to run the file as a program or script. The sign&nbsp;&nbsp;<code>!</code>&nbsp;indicates that the command is being executed in a Jupyter Notebook or similar environment. This command runs an executable file or script named&nbsp;&nbsp;<code>darksignature</code>, located in the current directory.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>!chmod +x darksignature
!./darksignature</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1251} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image-2.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1251"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>This is a command to run a program or script that is likely designed to manipulate Bitcoin digital signatures. The symbol&nbsp;&nbsp;<code>!</code>&nbsp;may indicate that the command is being executed in an environment that supports such commands (such as a terminal or console).&nbsp;<strong><code>-address</code></strong>: This is a command line option that tells the program that it is followed by a Bitcoin address. In this case, the address&nbsp;&nbsp;<code>14NWDXkQwcGN1Pd9fboL8npVynD5SfyJAE</code>&nbsp;is a string that is a unique identifier for a Bitcoin wallet. Once run, we get the result of the public key in HEX format.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>!./darksignature -address 14NWDXkQwcGN1Pd9fboL8npVynD5SfyJAE</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1252} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image-3-1024x83.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1252"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Result:</h3>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>pubkey: (HEX) = 04ca5606a1e820e7a2f6bb3ab090e8ade7b04a7e0b5909a68dda2744ae3b8ecbfa280a47639c811134d648e8ee8096c33b41611be509ebca837fbda10baaa1eb15</code></pre>
<!-- /wp:code -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>The command&nbsp;&nbsp;<code>!pip install ecdsa</code>&nbsp;is used to install the library&nbsp;&nbsp;<code>ecdsa</code>&nbsp;in the Python programming environment. The library&nbsp;&nbsp;<code>ecdsa</code>&nbsp;provides tools for working with the Elliptic Curve Digital Signature Algorithm (ECDSA). It allows you to create key pairs (private and public), sign messages, and verify signatures. The library allows you to check whether a message was actually signed by a certain key.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>!pip install ecdsa</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1253} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image-4-1024x121.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1253"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>This code allows you to extract the coordinates of a point on the elliptic curve from a Bitcoin public key.&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>from ecdsa import VerifyingKey, SECP256k1 
import binascii 

def get_coordinates_from_pubkey(pubkey_hex): 
    # Convert HEX to bytes 
    pubkey_bytes = binascii.unhexlify(pubkey_hex) 
    
    # Create a VerifyingKey object from the public key 
    vk = VerifyingKey.from_string(pubkey_bytes, curve=SECP256k1) 
    
    # Get the Gx and Gy coordinates 
    Gx = vk.pubkey.point.x() 
    Gy = vk.pubkey.point.y() 
    
    # Convert the coordinates to HEX format 
    Gx_hex = format(Gx, 'x').zfill(64) # Fill with zeros up to 64 characters 
    Gy_hex = format(Gy, 'x').zfill(64) # Fill with zeros up to 64 characters 
    
    return Gx_hex, Gy_hex 

pubkeyhex = "04ca5606a1e820e7a2f6bb3ab090e8ade7b04a7e0b5909a68dda2744ae3b8ecbfa280a47639c811134d648e8ee8096c33b41611be509ebca837fbda10baaa1eb15" 

Gx, Gy = get_coordinates_from_pubkey(pubkeyhex) 

print(f"pubkey: {pubkeyhex}") 
print(f"") 
print(f"(Gx, Gy) = {Gx} {Gy}")
</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1254} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image-5-1024x466.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1254"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Result:</h3>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>pubkey: 04ca5606a1e820e7a2f6bb3ab090e8ade7b04a7e0b5909a68dda2744ae3b8ecbfa280a47639c811134d648e8ee8096c33b41611be509ebca837fbda10baaa1eb15

(Gx, Gy) = ca5606a1e820e7a2f6bb3ab090e8ade7b04a7e0b5909a68dda2744ae3b8ecbfa 280a47639c811134d648e8ee8096c33b41611be509ebca837fbda10baaa1eb15</code></pre>
<!-- /wp:code -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>This is the command to run&nbsp;<strong><a href="https://github.com/smartibase/Broadcast-Bitcoin-Transaction/tree/main/darksignature">darksignature</a></strong>&nbsp;<strong><code>-pubkey</code></strong>&nbsp;: This is a command line option that tells the program that it is followed by a public key. The public key is used to verify signatures and identify the owner of funds in the Bitcoin network.&nbsp;<strong><code>ca5606a1e820e7a2f6bb3ab090e8ade7b04a7e0b5909a68dda2744ae3b8ecbfa</code></strong>: This is the first part of the command parameters - the coordinate&nbsp;&nbsp;<code>Gx</code>&nbsp;(x-coordinate) of the public key in hexadecimal format. It is a piece of information about the public key that is needed for cryptographic operations.&nbsp;<strong><code>280a47639c811134d648e8ee8096c33b41611be509ebca837fbda10baaa1eb15</code></strong>: This is the second part of the command parameters - the coordinate&nbsp;&nbsp;<code>Gy</code>&nbsp;(y-coordinate) of the public key, also in hexadecimal format. The result is the signature value R, S, Z.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>!./darksignature -pubkey ca5606a1e820e7a2f6bb3ab090e8ade7b04a7e0b5909a68dda2744ae3b8ecbfa 280a47639c811134d648e8ee8096c33b41611be509ebca837fbda10baaa1eb15
</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1255} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image-6-1024x102.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1255"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Result:</h3>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>|==========================================================================================================================================================================================================|
pubkey: (Gx , Gy) = (91519190036866233587583752863966343541024156557754641198598352460350806215674, 18110675123485594228049867696927871008716109164646265340106239137304742587157)
|===|================ Get ECDSA Signature: &lt;R&gt; value ================|================ Get ECDSA Signature: &lt;S&gt; value ================|================ Get ECDSA Signature: &lt;Z&gt; value ================|===|
1111,dc2e5e1104d74ace769d2c51901b6a6237c723a56aa4a295ea37ad826d0ddfbb,4785af2aeff25512213694d4cd1fe85ca21606cce8e43f34799d4af3b1cdf2b2,18a00b1802ee4d717ced01a782f89f509a2fac59376e1de4bde0c7f448869455,0000</code></pre>
<!-- /wp:code -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>This command writes to a file: Instead of displaying the text on the screen, it will be written to a file&nbsp;&nbsp;<code>SignRSZ.txt</code>. If this file does not exist before, it will be created.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>!echo '1111,dc2e5e1104d74ace769d2c51901b6a6237c723a56aa4a295ea37ad826d0ddfbb,4785af2aeff25512213694d4cd1fe85ca21606cce8e43f34799d4af3b1cdf2b2,18a00b1802ee4d717ced01a782f89f509a2fac59376e1de4bde0c7f448869455,0000' &gt; SignRSZ.txt
</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1256} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image-7-1024x57.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1256"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>Run the&nbsp;<a href="https://github.com/smartibase/Broadcast-Bitcoin-Transaction/blob/main/darksignature/calculatenonce.py" target="_blank" rel="noreferrer noopener"><strong>calculatenonce.py</strong></a>&nbsp;script to get the&nbsp;<strong>Secret Key NONCE</strong>&nbsp;value in HEX format</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>!python calculatenonce.py</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1257} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image-8.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1257"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Result:</h3>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>Secret Key  NONCE:  db7bbcb93e3fb5259c5035c6321134b60b8b5afb37cff08641ce3ebbf8e1a95c
Signatere R value:  dc2e5e1104d74ace769d2c51901b6a6237c723a56aa4a295ea37ad826d0ddfbb</code></pre>
<!-- /wp:code -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Secret Key NONCE</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Secret Key&nbsp;</strong>&nbsp;<strong>(NONCE)</strong>&nbsp;is a value in cryptography that is used to encrypt and sign data. In the context of Bitcoin, the secret key allows the user to control their&nbsp;<strong>BTC</strong>&nbsp;coins .</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Let's run the command to get the public key for the secret key value&nbsp;<strong>(NONCE)</strong></p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>!./darksignature -privkey db7bbcb93e3fb5259c5035c6321134b60b8b5afb37cff08641ce3ebbf8e1a95c</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1258} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image-9-1024x73.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1258"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Result:</h3>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>pubkey: (HEX) = 04dc2e5e1104d74ace769d2c51901b6a6237c723a56aa4a295ea37ad826d0ddfbb384139c65187ffece2e0c880f013cb69ede7d9078ef6c68d1eafbec50ec05502</code></pre>
<!-- /wp:code -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Signatere R value &amp; pubkey: (HEX)</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Let's check if the&nbsp;<strong>R</strong>&nbsp;value of the signature and the&nbsp;<strong>Gx</strong>&nbsp;coordinate of the public key are the same, then the Bitcoin transaction signature is valid.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":1259} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/11/image-10-1024x113.png" alt="DarkSignature is a tool for creating fake signature values ​​in Bitcoin cryptocurrency" class="wp-image-1259"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Result:</h3>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>  dc2e5e1104d74ace769d2c51901b6a6237c723a56aa4a295ea37ad826d0ddfbb
04dc2e5e1104d74ace769d2c51901b6a6237c723a56aa4a295ea37ad826d0ddfbb384139c65187ffece2e0c880f013cb69ede7d9078ef6c68d1eafbec50ec05502</code></pre>
<!-- /wp:code -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p><a href="https://github.com/smartibase/Broadcast-Bitcoin-Transaction/tree/main/darksignature"><strong>The DarkSignature</strong></a>&nbsp;tool&nbsp;is a powerful tool for creating fake signature values ​​in the Bitcoin cryptocurrency by exploiting vulnerabilities in cryptographic algorithms such as ECDSA.&nbsp;<strong>DarkSignature</strong>&nbsp;can generate invalid signatures that can be accepted as valid by the system, posing serious threats to user security and network integrity. When using&nbsp;<a href="https://github.com/smartibase/Broadcast-Bitcoin-Transaction/tree/main/darksignature"><strong>DarkSignature,</strong></a>&nbsp;users can modify directories, install necessary libraries, and extract public key coordinates, allowing them to manipulate digital signatures. These actions highlight the importance of carefully checking and protecting the cryptographic mechanisms used in Bitcoin and other cryptocurrencies. Understanding how tools like&nbsp;<a href="https://github.com/smartibase/Broadcast-Bitcoin-Transaction/tree/main/darksignature"><strong>DarkSignature</strong></a>&nbsp;work helps raise awareness of potential risks and vulnerabilities in the system, which is essential for ensuring security in the world of digital currencies.</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p><strong>Source code:&nbsp;<a href="https://github.com/smartibase/Broadcast-Bitcoin-Transaction/tree/main/darksignature" target="_blank" rel="noreferrer noopener">https://github.com/smartibase/Broadcast-Bitcoin-Transaction/tree/main/darksignature</a></strong></p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p><a href="https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpolynonce.ru%2Fdarksignature%2F" target="_blank" rel="noreferrer noopener"></a><a href="http://twitter.com/share?url=https%3A%2F%2Fpolynonce.ru%2Fdarksignature%2F&amp;text=DarkSignature%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8%20%D0%B2%20%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B5%20%D0%91%D0%B8%D1%82%D0%BA%D0%BE%D0%B9%D0%BD" target="_blank" rel="noreferrer noopener"></a><a href="mailto:?subject=DarkSignature%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8%20%D0%B2%20%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B5%20%D0%91%D0%B8%D1%82%D0%BA%D0%BE%D0%B9%D0%BD&amp;body=https%3A%2F%2Fpolynonce.ru%2Fdarksignature%2F" target="_blank" rel="noreferrer noopener"></a><a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fpolynonce.ru%2Fdarksignature%2F&amp;title=DarkSignature%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8%20%D0%B2%20%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B5%20%D0%91%D0%B8%D1%82%D0%BA%D0%BE%D0%B9%D0%BD" target="_blank" rel="noreferrer noopener"></a><a href="https://telegram.me/share/url?url=https%3A%2F%2Fpolynonce.ru%2Fdarksignature%2F&amp;text&amp;title=DarkSignature%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8%20%D0%B2%20%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B5%20%D0%91%D0%B8%D1%82%D0%BA%D0%BE%D0%B9%D0%BD" target="_blank" rel="noreferrer noopener"></a><a href="javascript:pinIt();"></a><a href="javascript:window.print()"></a></p>
<!-- /wp:paragraph -->
