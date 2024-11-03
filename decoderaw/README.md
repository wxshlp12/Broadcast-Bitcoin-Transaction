<!-- wp:image {"id":1216} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/10/image-9.png" alt="DecodeRaw tool for decoding RawTX in Bitcoin cryptocurrency" class="wp-image-1216"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Decoding&nbsp;<code>RawTX</code>is&nbsp;<code>Bitcoin</code>the process of converting raw transaction data (in the form of a hexadecimal string) into a understandable format that allows you to see transaction details such as inputs, outputs, and addresses.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What is RawTX?</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong><code>RawTX</code></strong>&nbsp;(raw transaction) is the raw format of a Bitcoin transaction that includes all the data needed to perform the transaction, but is not interpreted by the Bitcoin client. It is usually represented as a hexadecimal string.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Why do you need decoding?</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Decoding RawTX allows you to:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>Check transaction details</strong>&nbsp;: see sender and recipient addresses, amounts and other parameters.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Debug transactions</strong>&nbsp;: Developers can use decoding to analyze and fix errors in their transactions.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Analyze security</strong>&nbsp;: Security researchers can look for vulnerabilities or anomalies in transaction structures.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">How does decoding happen?</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Receiving RawTX</strong>&nbsp;: First, you need to obtain the raw transaction, which can be received from a Bitcoin node or created manually.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This command changes the current directory to&nbsp;&nbsp;<code>decoderaw</code>. This means that all subsequent commands will be executed in this folder. If the necessary scripts or programs for decoding transactions are in it, this will allow them to be used. The command&nbsp;&nbsp;<code>ls</code>&nbsp;lists all files and directories in the current directory (in this case,&nbsp;&nbsp;<code>decoderaw</code>). This is useful for checking for files or scripts that may be needed for further actions. By default, the command does not show hidden files (those that begin with a dot).</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>cd decoderaw/

ls
</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1213} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/10/image-6.png" alt="DecodeRaw tool for decoding RawTX in Bitcoin cryptocurrency" class="wp-image-1213"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>This command changes the permissions of a file or directory&nbsp;&nbsp;<code>decoderaw</code>by adding execute permission (&nbsp;<code>+x</code>). This is necessary if you want to run the file as a program or script. The sign&nbsp;&nbsp;<code>!</code>&nbsp;indicates that the command is being executed in a Jupyter Notebook or similar environment. This command runs an executable file or script named&nbsp;&nbsp;<code>decoderaw</code>, located in the current directory. If it is a program to decode RawTX, it will begin executing and may wait for input or parameters.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>!chmod +x decoderaw
!./decoderaw</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1214} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/10/image-7.png" alt="DecodeRaw tool for decoding RawTX in Bitcoin cryptocurrency" class="wp-image-1214"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>This command runs the script&nbsp;&nbsp;<code>decoderaw</code>&nbsp;with an argument&nbsp;&nbsp;<code>0100000001db768ce7346503b8463a30bb.....ff1652223eba47388ac00000000</code>, which is a raw Bitcoin transaction (RawTX). The script should decode this string and output transaction information such as inputs and outputs, addresses, and amounts. Thus, these commands allow the user to work with RawTX Bitcoin and extract useful information from it through decoding.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>!./decoderaw 0100000001db768ce7346503b8463a30bb23b31958d93e6b8575313cda27f888e1b4fd292a000000008b483045022100f52eac6791aad6361899400b65f48727a20398ba7d64ce0e3eaa85ae2d379583022031748b2e7468be1c476efe6079b9fab4d7aba12cd91ee26a177cbaabc306419a014104ca5606a1e820e7a2f6bb3ab090e8ade7b04a7e0b5909a68dda2744ae3b8ecbfa280a47639c811134d648e8ee8096c33b41611be509ebca837fbda10baaa1eb15ffffffff0258020000000000001976a914d74de95f65799793f16b91ed8a152110652d3ec088acaa20cf01000000001976a91424f98038e995ee03c4178bccaff1652223eba47388ac00000000
</code></pre>
<!-- /wp:code -->

<!-- wp:image {"id":1215} -->
<figure class="wp-block-image"><img src="https://polynonce.ru/wp-content/uploads/2024/10/image-8-1024x140.png" alt="DecodeRaw tool for decoding RawTX in Bitcoin cryptocurrency" class="wp-image-1215"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Result:</h2>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>Result:

1111,00f52eac6791aad6361899400b65f48727a20398ba7d64ce0e3eaa85ae2d379583,31748b2e7468be1c476efe6079b9fab4d7aba12cd91ee26a177cbaabc306419a,1098deb834849157a372372447f4e168c77daf6592fb37276ad68541a3e1fbcf,0000


</code></pre>
<!-- /wp:code -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p><code>Signature RSZ&nbsp;</code>In the context of RawTX decoding, Bitcoin refers to the values ​​that represent the components of the digital signature used in the ECDSA (Elliptic Curve Digital Signature Algorithm) algorithm. These values ​​help to verify the authenticity of transactions.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading"><strong><code>RSZ</code></strong>&nbsp;consists of three components:</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong><code>R</code></strong>: This is a value that is part of the signature and is generated based on a random number chosen when signing.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong><code>S</code></strong>: This is the second value of the signature, which depends on R and other transaction data.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong><code>Z</code></strong>: This is a hash of the message (or transaction) that is being signed. It is created from the transaction data and is used to ensure integrity and authenticity.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p><strong>Source code:</strong>  <strong><a href="https://github.com/smartibase/Broadcast-Bitcoin-Transaction/tree/main/decoderaw" target="_blank" rel="noreferrer noopener">https://github.com/smartibase/Broadcast-Bitcoin-Transaction/tree/main/decoderaw</a></strong></p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->
